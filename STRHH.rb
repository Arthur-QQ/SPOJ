gets.to_i.times do 
    word = gets.chomp
    first_half = word[0, word.length / 2]
    for i in (0...first_half.length) do
        print first_half[i] if i % 2 == 0
    end
    puts
end
