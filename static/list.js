$('#userDetailTable').DataTable({

'deferRender': false,
"autoWidth": true,
data:window.data,
responsive:true,
dom:'Bfrtip',
lengthMenu:[
[5,10,25,50,-1],
['5rows','10rows','25rows','50rows','Showall']
],
buttons:[
'pageLength','copy','csv','excel','pdf'
],
select:true,
hover:true,
});
