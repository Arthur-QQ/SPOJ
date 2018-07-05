casoteste n = do
    if n > 0 then do
        val' <- getLine
        let val = read val' :: Int
        -- Sum{i=1..k}3i-1
        -- = Sum{i=1..k}3i - Sum{i=1..k}1
        -- = 3*(1 + k) * k / 2 - k
        let expr = div (3 * (val + 1) * val) 2 - val
        print(expr `mod` 1000007)
        casoteste (n-1)
    else
        return ""

main = do
    lines' <- getLine
    let lines = read lines' :: Int
    casoteste lines
