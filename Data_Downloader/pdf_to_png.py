import os, glob, mimetypes
from pathlib import Path
from pdf2image import convert_from_path 

# poppler/binを環境変数PATHに追加する
poppler_dir = Path(__file__).parent.absolute() / "poppler/bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)

img_dir = Path("data_img")

def main():
    # data_pdfディレクトリの中身を取得
    input_files = glob.glob("data_pdf/*")

    # data_pdfディレクトリの中身が空のとき、それを表示
    if not input_files:
        print("There is no input file.\n")

    # 一つずつ変換
    for file in input_files:
        file_fmt = mimetypes.guess_type(file)
        if file_fmt[0] == "application/pdf":
            # PDF -> Image に変換（200dpi）
            print("Converting " + file + " to png format")
            pages = convert_from_path(file, 200)

            # 画像ファイルを１ページずつ保存
            for i, page in enumerate(pages):
                file_name = Path(file).stem + "_{:03d}".format(i) + ".png"
                image_path = img_dir / file_name
                page.save(str(image_path), "PNG")

            print("Conversion completed!\n")
        
        else:
            print(file + " is not in pdf format!\n")

if __name__ == "__main__":
    main()
