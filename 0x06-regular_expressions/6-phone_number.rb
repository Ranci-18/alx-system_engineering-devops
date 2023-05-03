#!/usr/bin/env ruby
#Ruby script accepts one argument and passes it
#to a regular expression mathing method
#to match a 10 digit phone number

puts ARGV[0].scan(/\A\d{10}\z/).join
