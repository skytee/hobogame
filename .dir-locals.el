 ;; The 'nil' configuration applies to all modes.
    ((nil . ((indent-tabs-mode . t)
            (tab-width . 2)))
     (python-mode . (
            ;; Highlight leading space characters in Python files.
		      (eval . (highlight-regexp "^ *")))))
