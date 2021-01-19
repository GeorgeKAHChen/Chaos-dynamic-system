#Auto Latex Compile
#Copyright by Kazuki Amakawa

filename=English
main:
	xelatex ${filename}.tex
	xelatex ${filename}.tex
	xelatex ${filename}.tex
	rm -rf ${filename}.{ps,log,aux,out,dvi,bbl,blg,thm,toc,nav,snm}
	open ${filename}.pdf

init:
	open ./
	open /Applications/Slack.app
	open /System/Applications/Calendar.app
	open /System/Applications/Mail.app
	open ${filename}.tex
	xelatex ${filename}.tex
	xelatex ${filename}.tex
	xelatex ${filename}.tex
	rm -rf ${filename}.{ps,log,aux,out,dvi,bbl,blg,thm,toc,nav,snm}
	open ${filename}.pdf


ref:
	xelatex ${filename}.tex
	bibtex ${filename}.aux
	xelatex ${filename}.tex
	xelatex ${filename}.tex
	rm -rf ${filename}.{ps,log,aux,out,dvi,bbl,blg,thm,toc,nav,snm}
	open ${filename}.pdf

e:
	xelatex ${filename}.tex
	rm -rf ${filename}.{ps,log,aux,out,dvi,bbl,blg,thm,toc,nav,snm}
	open ${filename}.pdf

clear:
	rm -rf ${filename}.pdf
