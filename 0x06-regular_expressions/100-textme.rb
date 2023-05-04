#!/usr/bin/env ruby
#Ruby script runs statistics on the TextMe app
#text messages transactions

puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
