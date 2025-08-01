import random
from typing import List

# 運勢リストを定数として定義
FORTUNES: List[str] = ["大吉", "吉", "中吉", "小吉", "末吉", "凶"]

def draw_omikuji() -> str:
    """
    おみくじを引いて、結果を返す関数。
    """
    return random.choice(FORTUNES)
