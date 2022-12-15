# Start Safe Exam Browser in a new process
$sebProcess = Start-Process -FilePath "C:\Program Files\SafeExamBrowser\Application\SafeExamBrowser.exe" -ArgumentList "/nosplash" -PassThru

# Set the Safe Exam Browser window to be a "non-locking" window
Add-Type -Name Window -Namespace Console -MemberDefinition @"
[DllImport("user32.dll")]
public static extern int SetWindowLong(IntPtr hWnd, int nIndex, int dwNewLong);
"@

# Use the MainWindowHandle property of the Process object to get the window handle
$windowHandle = $sebProcess.MainWindowHandle

# Set the Safe Exam Browser window to be a "non-locking" window
$result = [Console.Window]::SetWindowLong($windowHandle, (-20), 0x20)

# Start the Safe Exam Browser process
$sebProcess.Start()
