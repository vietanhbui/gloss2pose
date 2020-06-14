# Gloss2Pose multimedia
Project multimedia nhóm 10

## Trước khi chạy
1. Tải tập gloss tại link: [google drive](https://drive.google.com/open?id=1-6mEINVrWKncQZP9BxfxecVVA4DszFSo). Sau đó copy file video-metadata.csv vào thư mục root của project `gloss2pose/video-metadata.csv`.
2. Tải tập pose [google drive](https://drive.google.com/open?id=1sRPA9nrA4sos6iy7bJoAl9kanyWeTz5D). Giải nén sẽ được folder lookup. Sau đó copy folder vào thư mục root của project `gloss2pose/lookup/`.
3. Sửa lại file json `gloss2pose/path.json` sao cho path phù hợp với 2 phần trên

## Run
1. Nhập gloss tại file `gloss2pose/input-gloss.txt`
2. Chạy file `gloss2pose/gloss2pose.py`.
3. Tập pose tương ứng sẽ được sinh ra tại `gloss2pose/lookup/conbined-pose.mov`