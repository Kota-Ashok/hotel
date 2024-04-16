<script>
  $(document).ready(function()
  {
    $('.chkcvalues').click(function()
    {
      var txt="";
      $('.chkcvalues:checked').each(function()
      {
        txt+=$(this).val()+","
      });
      $('#txtvalues').val(txt);
    })
  })
</script>