import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    # treeview Widgetの情報を格納する変数
    treeview = None

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、treeview Widgetを作成する。
        # columns : 各データ列へ名前を設定。
        self.treeview = ttk.Treeview(frame, columns=["colA", "colB", "colC"])

        #############################################
        # <各列に対してオプション設定>
        # #0 : 階層列(ツリーカラム)を意味する。
        # 階層列(ツリーカラム)のオプションを設定。
        # width : 幅の設定
        self.treeview.column("#0", width=100)
        # colA列のオプションを設定。
        # width : 幅の設定
        self.treeview.column("colA", width=80)
        # colB列のオプションを設定。
        # width : 幅の設定
        self.treeview.column("colB", width=80)
        # colC列のオプションを設定。
        # width : 幅の設定
        self.treeview.column("colC", width=80)
        #############################################

        #############################################
        # <各列の見出しに対してオプション設定>
        # #0 : 階層列(ツリーカラム)を意味する。
        # 階層列(ツリーカラム)の見出しを設定。階層列とする。
        self.treeview.heading("#0", text="階層列")
        # colA列の見出しを設定。データ列Aとする。
        self.treeview.heading("colA", text="データ列A")
        # colB列の見出しを設定。データ列Bとする。
        self.treeview.heading("colB", text="データ列B")
        # colC列の見出しを設定。データ列Cとする。
        self.treeview.heading("colC", text="データ列C")
        #############################################

        #############################################
        # <アイテムを挿入>
        # 第一引数 : 階層化する場合、親要素のアイテムIDを指定。階層化しない場合、""を指定する。
        # 第二引数 : どのindex(アイテム位置)へアイテムを挿入するのか指定する。tk.END : index(アイテムの最終位置)
        # text option : 階層列へ表示するアイテムの名前を設定。
        # open option : 子要素のアイテムを展開して表示するのかどうか設定する。True : 子要素のアイテムを展開して表示する, False : 子要素のアイテムを展開して表示しない、デフォルト。
        # values option : データ列へ表示する値を設定。
        # 戻り値 : アイテムID
        itemAId = self.treeview.insert("", tk.END, text="itemA", open=True, values=("data1a", "data1b", "data1c"))
        # 第一引数 : 階層化する場合、親要素のアイテムIDを指定。階層化しない場合、""を指定する。
        # 第二引数 : どのindex(アイテム位置)へアイテムを挿入するのか指定する。tk.END : index(アイテムの最終位置)
        # text option : 階層列へ表示するアイテムの名前を設定。
        # open option : 子要素のアイテムを展開して表示するのかどうか設定する。True : 子要素のアイテムを展開して表示する, False : 子要素のアイテムを展開して表示しない、デフォルト。
        # values option : データ列へ表示する値を設定。
        # 戻り値 : アイテムID
        itemBId = self.treeview.insert(itemAId, tk.END, text="itemB", open=True, values=("data2a", "data2b", "data2c"))
        # 第一引数 : 階層化する場合、親要素のアイテムIDを指定。階層化しない場合、""を指定する。
        # 第二引数 : どのindex(アイテム位置)へアイテムを挿入するのか指定する。tk.END : index(アイテムの最終位置)
        # text option : 階層列へ表示するアイテムの名前を設定。
        # values option : データ列へ表示する値を設定。
        # 戻り値 : アイテムID
        itemCId = self.treeview.insert(itemBId, tk.END, text="itemC", values=("data3a", "data3b", "data3c"))
        # 第一引数 : 階層化する場合、親要素のアイテムIDを指定。階層化しない場合、""を指定する。
        # 第二引数 : どのindex(アイテム位置)へアイテムを挿入するのか指定する。tk.END : index(アイテムの最終位置)
        # text option : 階層列へ表示するアイテムの名前を設定。
        # values option : データ列へ表示する値を設定。
        # 戻り値 : アイテムID
        itemDId = self.treeview.insert("", tk.END, text="itemD", values=("data4a", "data4b", "data4c"))
        #############################################

        # frame Widget(Frame)を親要素とした場合に、treeview Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.treeview.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
