import subprocess
from utils.config import BASE_DIR

def main():
    # 构建main.py的绝对路径
    main_script = BASE_DIR / "app" / "main.py"

    # 检查文件是否存在
    if not main_script.exists():
        raise FileNotFoundError(f"未找到应用入口文件:{main_script}")

    print(f"🔍 找到应用入口: {main_script}")
    print(f"🚀 启动飞机噪声预测系统...")
    
    # 启动Streamlit应用
    subprocess.run(
        ["streamlit", "run", str(main_script)],
        check=True,
        cwd=BASE_DIR  # 确保工作目录为项目根目录
    )


if __name__ == "__main__":
    main()
