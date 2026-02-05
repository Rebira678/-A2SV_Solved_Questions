#811. Subdomain Visit Count
#https://leetcode.com/problems/subdomain-visit-count/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        for i in range(len(cpdomains)):
            cpdomains[i]=list(cpdomains[i].split())
        container={}
        for i in range(len(cpdomains)):
            count=int(cpdomains[i][0])
            domain=cpdomains[i][1]
            if domain in container:
                container[domain]+=count
            else:
                container[domain]=count
            
            while "." in domain:
                domain=domain.split(".",1)[1]
                if domain in container:
                    container[domain]+=count
                else:
                    container[domain]=count
        ans=[]
        for k in container:
            ans.append(str(container[k])+" "+k)
        return ans
