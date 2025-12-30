import weakref
import cupy as np

# 1. オブジェクト作成
a = np.array([1, 2, 3])
b = weakref.ref(a)
print(b)
print(b())
# 2. 参照を削除
a = None

# 3. 確認
print(b)  # <weakref at ...; dead> と表示されれば成功
print(b()) # None と表示されれば、循環参照なく解放されています