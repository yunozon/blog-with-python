import os
import img2pdf

def images_to_pdf(images_folder_path, pdf_file_path):
    """
    フォルダにある画像をPDFに変換する
    Args:
        images_folder_path (str): 画像フォルダのパス
        pdf_file_path (str): 出力PDFファイルのパス
    """
    if not os.path.exists(images_folder_path):
        raise FileNotFoundError(f"指定された画像フォルダが見つかりません: {images_folder_path}")
    
    files = os.listdir(images_folder_path)
    # 画像ファイルのみをフィルタリング
    images = [os.path.join(images_folder_path, file) for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not images:
        raise FileNotFoundError(f"フォルダ内に画像ファイルが見つかりません: {images_folder_path}")
    
    # PDFの書き出し
    with open(pdf_file_path, "wb") as f:
        f.write(img2pdf.convert(images))
    print(f"PDFが正常に作成されました: {pdf_file_path}")

# 使用例
images_folder_path = "work/blog1/datasets1"  # 画像フォルダのパスを指定
pdf_file_path = "work/blog1/output.pdf"  # 出力PDFのファイル名を指定
images_to_pdf(images_folder_path, pdf_file_path)
