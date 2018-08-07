import os
import win32com.client

slide_directory = os.listdir('C:/Users/Abhishek/Desktop/ppt')
print slide_directory
ppt_list = []
for ppt in slide_directory:
	if ppt.endswith('.pptx') or ppt.endswith('.ppt'):
		ppt_list.append(ppt)
print ppt_list

Application = win32com.client.Dispatch("PowerPoint.Application")
Application.Visible = True

slide_count = 0
old_count = 0

for element in ppt_list:
	Presentation = Application.Presentations.Open(r'C:/Users/Abhishek/Desktop/ppt/'+element)

	slide_count = slide_count + len(Presentation.Slides)
	print (slide_count)

	for c in range(old_count, slide_count):
		Presentation.Slides[c-old_count].Export(r'C:\Users\Abhishek\Desktop\ppt\images\image{0}.jpg'.format(c), "JPG", 1366, 768)

	old_count = slide_count

Application.Quit()