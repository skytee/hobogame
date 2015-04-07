import pygame

def rendertext(text, font, fontcolor, backgroundcolor=None):

	m_width, m_height, line_no = 0, 0, 0 
	if not backgroundcolor:
		backgroundcolor = (0, 0, 0)
	fontheight = font.get_height()
	text_lines = text.splitlines(False)

	for line in text_lines:
		(width, height) = font.size(line)
		m_width = max (width, m_width)
		m_height += height

	textsurface = pygame.Surface((m_width, m_height))
	textsurface.convert()
	textsurface.fill(backgroundcolor)

	for line in text_lines:
		tmp_surface = font.render(line, 1, fontcolor, backgroundcolor)
		tmp_surface.convert()
		textsurface.blit(tmp_surface, (0, line_no*fontheight))
		line_no += 1
		
 	colorkey = textsurface.get_at((0,0))
	textsurface.set_colorkey(colorkey)

	return textsurface.copy()

