import zipfile
import os

def compress(file_path, zip_path):
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
            z.write(file_path, os.path.basename(file_path))
        print(f" Đã nén {file_path} thành {zip_path}")
    except Exception as e:
        print(f" Lỗi khi nén: {e}")

def decompress(zip_path, extract_dir):
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(extract_dir)
        print(f" Đã giải nén {zip_path} vào {extract_dir}")
    except Exception as e:
        print(f" Lỗi khi giải nén: {e}")

# --- Chương trình chính ---
print("1. Nén tệp")
print("2. Giải nén tệp")
ch = input("Chọn: ")

if ch == '1':
    f = input("Nhập đường dẫn tệp cần nén: ").strip()
    z = input("Nhập tên file zip muốn tạo: ").strip()
    compress(f, z)
elif ch == '2':
    z = input("Nhập đường dẫn file zip: ").strip()
    out = input("Nhập thư mục muốn giải nén vào: ").strip()
    decompress(z, out)
else:
    print(" Lựa chọn không hợp lệ.")
