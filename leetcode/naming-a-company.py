# valid name을 만들기 위해서 첫 글자가 다르고 첫 글자를 제외한 뒷 글자가 달라야 한다.
# 첫 글자, 나머지 글자를 prefix, suffix라고 하면
# prefix로 분류된 집합들을 만들었을 때
# 공통적인 suffix들을 제외한 원소들끼리 valid name을 만들 수 있다.


from collections import defaultdict
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        answer = 0
        prefixdic = defaultdict(set)

        for idea in ideas:
            prefix, suffix = idea[0], idea[1:]
            prefixdic[prefix].add(suffix)

        while len(prefixdic) > 1:
            inspectPrefix, inspectSuffix = prefixdic.popitem()

            validName = 0
            for prefix in prefixdic:
                intersect = len(inspectSuffix.intersection(prefixdic[prefix]))
                validName += (len(inspectSuffix) - intersect) * (
                    len(prefixdic[prefix]) - intersect
                )

            answer += validName

        return answer * 2
