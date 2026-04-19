"""圆面积示例（进阶版）

特性：
1) 函数化结构
2) 输入校验并返回详细错误原因
3) 支持输入 q / quit 退出程序
"""

from typing import Optional, Tuple

PI = 3.14159
QUIT_WORDS = {"q", "quit"}


def calc_circle_area(radius: float, pi: float = PI) -> float:
    """根据半径计算圆面积。"""
    if radius < 0:
        raise ValueError("radius must be non-negative")
    return pi * radius * radius


def parse_radius(raw_value: str) -> Tuple[Optional[float], Optional[str]]:
    """把用户输入转换为半径，并返回错误原因。

    Returns:
        (radius, error)
        - 成功时: (float, None)
        - 失败时: (None, 错误原因)
    """
    cleaned = raw_value.strip()

    if cleaned == "":
        return None, "输入为空，请输入一个非负数字。"

    try:
        radius = float(cleaned)
    except ValueError:
        return None, f"无法识别 '{raw_value}'，请输入数字（例如 3 或 2.5）。"

    if radius < 0:
        return None, f"半径不能为负数（你输入的是 {radius}）。"

    return radius, None


def prompt_radius() -> Optional[float]:
    """循环询问用户半径，支持输入 q/quit 退出。"""
    while True:
        raw_value = input("请输入圆的半径（输入 q 退出）：")

        if raw_value.strip().lower() in QUIT_WORDS:
            print("已退出程序。")
            return None

        radius, error = parse_radius(raw_value)
        if error is None:
            return radius

        print(f"输入无效：{error}")


def main() -> None:
    """程序入口。"""
    radius = prompt_radius()
    if radius is None:
        return

    area = calc_circle_area(radius)
    print(f"半径: {radius:.2f}")
    print(f"面积: {area:.4f}")


if __name__ == "__main__":
    main()
