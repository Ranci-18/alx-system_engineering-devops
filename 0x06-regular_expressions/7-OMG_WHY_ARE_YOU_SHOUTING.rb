#!/usr/bin/env ruby
#ruby script accepts one argument and passes it to
#a regular expression matching method
#matches only upper case characters

puts ARGV[0].scan(/[[:upper:]]/).join
