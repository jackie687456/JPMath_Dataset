
# pdfファイルのダウンロードとpngへの変換

## 動作確認済みのシステム要件
- Windows10
- Python3.9.7

## 操作手順
1. GoogleドライブのDataDownloaderフォルダの中身をすべて、ローカルのDataDownloaderディレクトリにダウンロード
2. pdfファイルのダウンロード  
	- (Windows)動作確認済み
	    1. data_downloader.batをダブルクリックで実行
	    2. data_pdfディレクトリにpdfファイルがダウンロードされていることを確認  
	- (Mac)動作未確認
	    1. 以下のコマンドをターミナルで実行し、data_downloaderの実行権限を付与  
	        > chmod u+x ファイルパス/data_downloader.command
	    2. data_downloader.commandをダブルクリックで実行
	    3. data_pdfディレクトリにpdfファイルがダウンロードされていることを確認
3. pngへの変換
	1. 「pdf2image」ライブラリをインストール<br>
	   > pip install pdf2image
	2. エディタ(VSCodeなど)でDataDownloaderディレクトリを開く
	3. pdf_to_png.pyを実行
	4. data_imgディレクトリにpngファイルが作成されていることを確認

## document_list.csvについて
document_list.csvにはデータセットに利用した学術論文のタイトル,雑誌タイトル,巻号,URLが記載されている.