# 네이트 실시간 이슈 제목 및 키워드 순위를
# BeatifulSoup를 사용하여 출력하시오
from bs4 import BeautifulSoup

html = """
<div class="bizCnt">
    <div class="isKeyword">
        <h4>실시간 이슈 키워드</h4>
        <ol class="isKeywordList" id="olLiveIssueKeyword">
            <li>코로나19</li>
            <li>우크라이나 전쟁</li>
            <li>물가 상승</li>
        </ol>
    </div>
</div>
"""

soup = BeautifulSoup(html, 'html.parser')

keyword_list = soup.select('#olLiveIssueKeyword > li')

for keyword in keyword_list:
    print(keyword.text)