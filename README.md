# EmailProviderChecker
Script checks for Microsoft and Google MX records. If neither are found, it checks for the same in the SPF records. If it identifies either it informs the user. 

If the information is found from the SPF record, it's possible that it is an older, no longer used, entry. But it's a low probability. 
