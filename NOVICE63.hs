flist :: [Integer]
flist = scanl (*) 1 [1..]
memoized_fact :: Int -> Integer
memoized_fact n = flist !! n


bi_coef :: Int -> Int -> Integer
bi_coef n k = div (memoized_fact n) ((memoized_fact k) * memoized_fact (n - k))

ans :: Int -> Integer
ans n | n == 1 = 1
      | otherwise = sum [bi_coef (k - 1) (k `div` 2) | k <- [2, 4..n]]

func n = do
    if n > 0 then do
        num' <- getLine
        let num = read num' :: Int
        let logarithm = floor $ logBase 2 (fromIntegral num)
        print(ans logarithm)
        func (n - 1)
    else do
        return ""

main = do
    lines' <- getLine
    let lines = read lines' :: Int
    func (lines)
