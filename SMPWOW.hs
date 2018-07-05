repeating :: Int -> String
repeating 0 = ""
repeating n = 'o' : repeating(n-1)


main = do
    a <- getLine
    let n = read a :: Int
    putStrLn('W' : repeating n ++ "w")
