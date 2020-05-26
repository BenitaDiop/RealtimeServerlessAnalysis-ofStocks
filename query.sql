with dp as (
  select *, row_number() over (parition by High, Hour order by Name, Hour, Timestamp) as rn 
from (
    select upper(dati.Name) as Name, 
	round(dati.High,2) as High, 
			dati.Hour as Hour, 
			ts as Timestamp from (select name as Name, 
						max(high) as High, 
						substring(ts,12,2) as Hour from  "04" 
      group by 1, 3
      order by 1, 3
      ) dati, "04" datii
    where dati.Name = datii.name and dati.Hour = substring(ts,12,2) and dati.high = datii.High
    order by Name, Hour) db3)
    select Name, High, Hour, Timestamp,
    Case
    when rn=1 then (select count(*) from dp i where i.High = ii.High and i.Hour = ii.Hour)
    else 0
    end as Recurrence
    from dp ii order by Name, Hour, Timestamp






