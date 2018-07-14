<!DOCTYPE html>
<html>
<head>
	<title>Welcome Form</title>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
</head>
<?php include "connection.php" ?>
<body style="padding: 20px;">
	<div style="margin-top: 100px;" class="row">
		<h1 class="text-center" style="margin-top:-70px;margin-bottom: 20px;">Welcome to Printing Kiosk</h1>
		<center><a href="index.php" class="btn btn-info" style="margin-top:-10px;margin-bottom: 10px;">Back to Previous Page</a></center>
		<div class="col-md-2"></div>
		<div class="col-md-4">
			<div class="panel panel-primary">
				<div class="panel-heading">Printing Kiosk Number of Paper Maintenance</div>
				<div class="panel-body">
					<form action="function.php" method="post">
						<?php 
						$q = mysqli_query($con, "SELECT * FROM papertbl limit 1");
						$rows = mysqli_fetch_array($q);
						?>
						<div class="form-group">
							<label>Number of Paper:</label>
							<div class="input-group">
								<input type="number" name="numberpaper" min="0" class="form-control" value="<?php echo $rows['numberpaper']; ?>">
								<span class="input-group-btn">
									<button type="submit" name="btnupdatepaper" class="btn btn-primary btn-flat">Update</button>
								</span>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>

		<div class="col-md-4">
			<div class="panel panel-primary">
				<div class="panel-heading">Sales of Printing Kiosk</div>
				<div class="panel-body">
					<table style="margin-top: 10px;" class="table table-bordered table-striped">
						<?php 
						$query = mysqli_query($con, "SELECT * FROM salestbl order by id desc");
						$counter = 0;
						$total = 0;
						if(mysqli_num_rows($query) > 0){
							?>
							<tr>
								<th>NO.</th>
								<th>File Name</th>
								<th>Credit</th>
								<th>Date Print</th>
							</tr>
							<?php while ($row = mysqli_fetch_array($query)) { $total += $row['credits']; ?>
							<tr>
								<td width="40"><?php echo $counter = $counter + 1; ?></td>
								<td><?php echo $row['filename'] ?></td>
								<td><?php echo $row['credits'] ?></td>
								<td><?php echo $row['dateprint'] ?></td>
							</tr>
							<?php } ?>
							<tr>
								<td colspan="2"><b>Total:</b></td>
								<td class="text-center"><?php echo $total; ?></td>
								<td></td>
							</tr>
							<?php }else { echo "<div style='margin-top: 10px;' class='alert alert-danger'>No date found.</div>"; } ?>
						</table>
					</div>
				</div>
			</div>
			<div class="col-md-2"></div>
		</div>
	</body>
	<script type="js/jquery-2.2.3.min.js"></script>
	</html>