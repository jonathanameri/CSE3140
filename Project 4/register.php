<html>
<body>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
<div class="wrapper" style="width: 30%; margin: 0 auto;">
	<form class="form-signin" action='#' method="post">
		<h2 class="form-signin-heading">User Registration</h2><br/>
		<input type="text" class="form-control" name="username" placeholder="username" required="" autofocus="" /><br/>
		<input type="password" class="form-control" name="password1" placeholder="Password" required=""/><br/>
		<input type="password" class="form-control"name="password2"placeholder="Re-enter your password" required=""/><br/>
      	<button class="btn btn-small btn-primary btn-block" type="submit">Register</button>
	</form>

<?php
if($_POST['username']){
	$name = $_POST['username'];
	$password1 = $_POST['password1'];
	$password2 = $_POST['password2'];
	if($password1 == $password2){
		$handle = fopen("auth.txt", "a");
		$password_encrypted = md5($password1);
		fwrite($handle, $name . ":" . $password_encrypted . "\n");
		fclose($handle);
		echo "<b>Success!</b>";
	}
	else{
		echo "<b>Passwords don't match</b>";
	}
}
?>
</div>

</body>
</html>