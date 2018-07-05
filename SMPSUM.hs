main = do
    linha <- getLine
    let listinha = map (read::String->Int) (words linha)
    let a = listinha !! 0
    let b = listinha !! 1
    print(sum [i * i | i <- [a..b]])
