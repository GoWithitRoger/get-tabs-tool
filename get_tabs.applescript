tell application "Safari"
	set output to ""
	set a to every window
	repeat with w in a
		set b to every tab of w
		repeat with t in b
			set output to output & (get name of t) & "|||" & (get URL of t) & "\n"
		end repeat
	end repeat
end tell

return output