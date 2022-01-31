import os.path as osp
import glob

rootpath = "./data/JPMathDataset/train/"

xml_path_template = osp.join(rootpath + "xml/" + "*.xml")
xml_path_list = glob.glob(xml_path_template)

for xml_path in xml_path_list:
    with open(xml_path) as f:
        data_lines = f.read()

    # 文字列置換
    data_lines = data_lines.replace("InlineMF", "inlinemf")
    data_lines = data_lines.replace("DisplayMF", "displaymf")

    # 同じファイル名で保存
    with open(xml_path, mode="w") as f:
        f.write(data_lines)