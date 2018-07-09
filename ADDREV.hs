func n = do
    if n > 0 then do
        -- ...
        line' <- getLine
        let vars = words line'
        let a = read . reverse $ vars !! 0 :: Int
        let b = read . reverse $ vars !! 1 :: Int
        let c = a + b
        let ans = read . reverse . show $ c :: Int
        print(ans)
        func (n - 1)
    else
        return ""

main = do
    lines' <- getLine
    let lines = read lines' :: Int
    func lines
