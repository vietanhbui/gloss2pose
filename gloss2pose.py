import os
import pandas as pd
from subprocess import Popen, PIPE, CalledProcessError
import json


def run_bash_cmd(cmd):
    p = Popen(cmd, shell=True)
    output, error = p.communicate()
    if p.returncode != 0:
        raise CalledProcessError(p.returncode, cmd, output, stderr=error)


def get_pose_ids(gloss_filepath, gloss):
    pwd = os.getcwd()
    os.chdir(os.path.dirname(gloss_filepath))
    videos = pd.read_csv(os.path.basename(gloss_filepath))
    os.chdir(pwd)
    pose_ids = list()
    videos["Gloss Variant"] = videos["Gloss Variant"].apply(
        lambda x: x.rstrip("+")
    )
    for term in gloss:
        ids = videos[videos["Gloss Variant"] == term]["id"].values
        if len(ids) > 0:
            pose_ids.append(ids[0])
    return pose_ids


def write_concat_input_file(video_filepaths, input_filepath):

    with open(input_filepath, "w") as file_obj:
        for filepath in video_filepaths:
            file_obj.write("file 'lookup\{}'\n".format(filepath))

    return input_filepath


def concat_videos(video_filepaths, output_filepath):
    input_filepath = os.path.join(
        os.path.dirname(video_filepaths[0]),
        "input.txt"
    )
    video_filenames = [os.path.basename(f) for f in video_filepaths]
    write_concat_input_file(video_filenames, input_filepath)

    unformatted_cmd = "ffmpeg -f concat -safe 0 -i {} -codec copy -y {}"

    cmd = unformatted_cmd.format(
        input_filepath,
        output_filepath
    )
    run_bash_cmd(cmd)
    return output_filepath


def get_pose_files(lookup_folder, pose_ids):
    pose_filepaths = []
    for pose_id in pose_ids:
        pose_filename = "pose-{}.mov".format(pose_id)
        pose_filepath = os.path.join(lookup_folder, pose_filename)
        pose_filepaths.append(pose_filepath)
    return pose_filepaths


def video_to_jpg(video_filepath, jpg_directory):
    unformatted_cmd = "ffmpeg -i {} {} -hide_banner"

    cmd = unformatted_cmd.format(
        video_filepath,
        os.path.join(jpg_directory, "video-%06d.jpg")
    )

    run_bash_cmd(cmd)

    return jpg_directory


if __name__ == "__main__":
    with open("input-gloss.txt", "r") as file_obj:
        gloss = file_obj.read().strip().split()
    with open('path.json') as path_file:
        data = json.load(path_file)
    video_metadata_file_path = data['video_metadata_file_path']
    pose_ids = get_pose_ids(video_metadata_file_path, gloss)
    print(pose_ids)
    lookup_folder = data['lookup_folder']
    pose_filepaths = get_pose_files(lookup_folder, pose_ids)
    combined_video_filepath = os.path.join(
        os.path.dirname(pose_filepaths[0]), "combined-pose.mov")
    concat_videos(pose_filepaths, combined_video_filepath)
    jpg_directory = os.path.join(
        os.path.dirname(combined_video_filepath),
        "jpg/"
    )

    os.makedirs(jpg_directory, exist_ok=True)

    video_to_jpg(combined_video_filepath, jpg_directory)
