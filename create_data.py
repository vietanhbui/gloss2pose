def read_spa():
    file_spa = open("dataset/spa.txt", encoding='UTF-8')
    lines = file_spa.read().strip().split('\n')
    engs = []
    for line in lines:
        eng = line.split("\t")[0][:-1]
        if len(eng.split(" ")) > 1:
            engs.append(eng)
    return engs[::-1]


def read_gp():
    file_spa = open("dataset/gp_origin.txt", encoding='UTF-8')
    lines = file_spa.read().strip().split('\n')
    gps = []
    for line in lines:
        gp = []
        line_split = line.split("\t")
        g = line_split[1].strip()
        p = line_split[0].strip()
        gp = [g, p]
        gps.append(gp)
    return gps


if __name__ == "__main__":
    engs = read_spa()
    gps = read_gp()

    eng_gp = []
    for eng in engs[:2000]:
        eng_split = eng.split(" ")
        eng = ""
        pose = ""
        for eng_word in eng_split:
            for gp in gps:
                if gp[0].upper() == eng_word.upper():
                    eng = eng + " " + gp[0].upper()
                    pose = pose + " " + gp[1]
                    break
        eng_gp.append([pose.strip(), eng.strip()])
    with open("dataset/new_gp_origin.txt", "w") as file_obj:
        for line in eng_gp:
            file_obj.write("{}\t{}\n".format(line[0], line[1]))
    print("OK!")
        
        

