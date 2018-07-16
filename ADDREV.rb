def soma(arr)
	sominha = 0
	arr.each {|x| sominha += x }
	return sominha
end

gets.to_i.times do
    puts soma((gets.split.map {|x| x.reverse.to_i})).to_s.reverse.to_i
end
