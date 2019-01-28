%# wish_table.tpl
<p>The open wish items are as follows:</p>
<table border="1">
%for r in rows:
  <tr>
  %for c in r:
    <td>{{c}}</td>
  %end
  </tr>
%end
</table>