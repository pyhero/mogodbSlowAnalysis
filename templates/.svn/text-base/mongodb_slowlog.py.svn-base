
html_str ='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <title>MongoDB Slow Log</title>
    <!-- Bootstrap core CSS -->
    <!--
    <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="http://cdn.datatables.net/1.10.9/css/jquery.dataTables.min.css">
    -->
    <link rel="stylesheet" href="bootstrap.min.css">
    <link rel="stylesheet" href="bootstrap-theme.min.css">
    <link rel="stylesheet" href="jquery.dataTables.min.css">
    <!--[endif]-->
</head>
<body>
<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">MongoDB Slow Log</a>
        </div>
    </div>
</nav>
<div class="container-fluid">
    <div class="row">
        <div class="col-sm-9 col-sm-offset-1 col-md-10 col-md-offset-1 main">
            <br><br><br><br>
            <h4 class="page-header" style="display: inline">IP:{{ db_info.host }}</h4>&nbsp;&nbsp;
            <h4 class="page-header" style="display: inline">port:{{ db_info.port }}</h4>&nbsp;&nbsp;
            <br><br>
            <div class="table-responsive">
                <table id="myTable" class="table table-striped">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Namespace</th>
                        <th>Option</th>
                        <th>Query</th>
                        <th>Millis</th>
                        <th>Nscanned</th>
                        <th>Nreturned</th>
                        <th>ResponseLength</th>
                        <th>Ts</th>
                    </tr>
                    </thead>
                    <tbody>
                    {% for item in db_info.slow_log %}
                    {% for i in item %}
                    <tr>
                        <td>{{ loop.index }}</td>
                        <td>{{ i.ns }}</td>
                        <td>{{ i.op }}</td>
                        <td>{{ i.query }}</td>
                        <td>{{ i.millis }}</td>
                        <td>{{ i.nscanned }}</td>
                        <td>{{ i.nreturned }}</td>
                        <td>{{ i.responseLength }}</td>
                        <td>{{ i.ts }}</td>
                    </tr>
                    {% endfor %}
                    {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<!--
<script src="http://cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
<script src="http://cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<script src="http://cdn.datatables.net/1.10.9/js/jquery.dataTables.min.js"></script>
-->
<script src="jquery.min.js"></script>
<script src="bootstrap.min.js"></script>
<script src="jquery.dataTables.min.js"></script>
<script type="text/javascript">
    $('#myTable').DataTable( {
        select: true
    } );
</script>
</body>
</html>
'''