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
~
~
~
~
~
~
"register.php" 33L, 1151C                                        3,1           All
cse@cse3140-HVM-domU:/var/www/html$ ls
              break;
            }
          }
          $match = 2;
        }

        if($match == '1') {
           echo "<b>Login Success!</b>";
        $name = $username;
        $content = $_POST['commentContent'];
        if($content == "#CLEAR"){
                $handle = fopen("comments.html", "w");
                fwrite($handle, "");
                fclose($handle);
        }
        else{
        $handle = fopen("comments.html", "a");
        #"w" tow write to file "a" for appending
        fwrite($handle, "<b>" . $name . "</b>:<br/>" . $content . "<br/>");
        fclose($handle);
        }

        }
        if($match == '2') {
           echo "<b>Login Failed!</b>";
        }
        fclose($fh);
    }
    if($_POST['username']) {
        check_password($_POST['username'], $_POST['password']);
    }
    ?>
</div>

<p style="text-align:center;">Don't have an account? <a href="register.php">Register Now</a></p>

<div class="wrapper" style="width: 50%; margin: 0 auto; border-style: solid;">
<?php include "comments.html"; ?>
<!-- including "comments.html" means the page will display the contents of comments.html-->
</div>
</body>
</html>
"index.php" 88L, 2945C                                           76,5          Bot

<html>
<body>
<div class="wrapper" style="text-align:center;">
<h1>Welcome to my page</h1>

<div>
<p><em>Today's date is</em></p>
<p id = "current_date2">
</p>
</div>

<script>
date = new Date();
year = date.getFullYear();
month = date.getMonth() + 1;
day = date.getDate();
document.getElementById("current_date2").innerHTML = month + "/" + day + "/" + year;
</script>

<p>Lab 4 Web-Security Section 4 Group 13<br>
We are Jonathan Ameri and Hunter Krasnicki</p>
<button type="button" onclick="alert('Hello World it\'s section 4 group 13 - Jonathan Ameri + Hunter Krasnicki')">Click me!</button>
</div>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
<div class="wrapper" style="width: 30%; margin: 0 auto;">
    <form class="form-signin" action='#' method="post">
      <h2 class="form-signin-heading">User Login</h2><br/>
      <input type="text" class="form-control" name="username" placeholder="username" required="" autofocus="" /><br/>
      <input type="password" class="form-control" name="password" placeholder="Password" required=""/><br/>
        <input type="text" class="form-control"name="commentContent"placeholder="Enter your comment" required=""/><br/>
      <button class="btn btn-small btn-primary btn-block" type="submit">Login</button>
    </form>
    <?php
    function check_password($username, $password){
        $pwd_file = 'auth.txt';