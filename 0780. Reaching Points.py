class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx < sx or ty < sy: return False
        while sx < tx and sy < ty: tx, ty = tx % ty, ty % tx
        if tx == sx:
            return (ty - sy) % sx == 0
        elif ty == sy:
            return (tx - sx) % sy == 0
        else:
            return False