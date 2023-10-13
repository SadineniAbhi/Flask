from basic import Parents,Children,Sibling,db

surya = Parents.query.filter_by(p_name = "surya").first()
subba = Parents.query.filter_by(p_name = "subba").first()
anil = Parents.query.filter_by(p_name = "anil").first()

