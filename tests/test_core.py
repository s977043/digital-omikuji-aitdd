from omikuji_app.core import draw_omikuji, FORTUNES

def test_draw_omikuji_returns_valid_fortune():
    """
    draw_omikuji() は有効な運勢（文字列）を返すことをテストする。
    """
    # おみくじを引く
    fortune = draw_omikuji()

    # 返り値が文字列であることを確認
    assert isinstance(fortune, str)

    # 返り値が指定された運勢リストに含まれていることを確認
    assert fortune in FORTUNES