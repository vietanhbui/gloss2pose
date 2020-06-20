# Gloss2Pose multimedia
Project multimedia nhóm 10

## Trước khi chạy (ASL)
1. Chạy file `gloss2pose/train.ipynb` để thực hiện train dữ liệu (dùng colab). Sau khi train xong được folder training_checkpoints, tải về và đặt tại thư mục gốc của project `gloss2pose/training_checkpoints/`.
2. Tải tập pose [google drive](https://drive.google.com/open?id=1sRPA9nrA4sos6iy7bJoAl9kanyWeTz5D). Giải nén sẽ được folder lookup. Sau đó copy folder vào thư mục root của project `gloss2pose/lookup/`.
3. Sửa lại file json `gloss2pose/path.json` sao cho phù hợp với đường dẫn của máy tính

## Run
1. Nhập gloss tại file `gloss2pose/input/gloss.txt`
2. Chạy file `gloss2pose/main.py`.
3. Chuỗi pose tương ứng sẽ được sinh ra tại `gloss2pose/output/`