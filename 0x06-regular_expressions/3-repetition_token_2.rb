#!/usr/bin/env ruby
#Ruby script accepts one argument and passes it to
#a regular expression matching method

puts ARGV[0].scan(/hbt{1,4}n/).join
