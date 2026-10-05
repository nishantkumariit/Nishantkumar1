set -e
cd /tmp/claude-0/-home-user-Nishantkumar1/bfcd13db-6e92-51d7-93f0-7c69b2cf25bb/scratchpad/c7
P=/usr/local/lib/python3.11/dist-packages/pypandoc/files/pandoc
O=/root/.claude/skills/synced/78c4afc9-330c-4c26-a6b5-3cb5706540ac_95ec6797-5b32-4bd7-ba7a-7deff46f9727/docx/scripts
$P blocks.md -f markdown -t docx --reference-doc=orig.docx -o blocks.docx
unzip -q -o blocks.docx -d bl
rm -rf work; mkdir work; unzip -q orig.docx -d work
python3 $O/merge_runs.py work/ | tail -1
python3 edit7.py | cut -c1-60
python3 post7.py
rm -f work/word/media/image1.png work/word/media/image2.png
sed -i 's#<Relationship Id="rId11" [^>]*/>##; s#<Relationship Id="rId12" [^>]*/>##' work/word/_rels/document.xml.rels
python3 schemafix.py
rm -f ch7_out.docx; (cd work && zip -qXr ../ch7_out.docx '[Content_Types].xml' _rels docProps word)
python3 $O/office/validate.py ch7_out.docx 2>&1 | grep -i 'fail\|passed - no new\|all validations' | head
timeout 300 python3 $O/office/soffice.py --headless --convert-to pdf --outdir pdf ch7_out.docx >/dev/null 2>&1
pdfinfo pdf/ch7_out.pdf | grep Pages; pdftotext -layout pdf/ch7_out.pdf pdf/ch7_out.txt
