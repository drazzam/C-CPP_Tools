# Start Safe Exam Browser in a new process
Start-Process -FilePath "C:\Program Files\SafeExamBrowser\Application\SafeExamBrowser.exe" -ArgumentList "/nosplash"

# Set the Safe Exam Browser window to be a "non-locking" window
$sebWindow = Get-Process | Where-Object {$_.ProcessName -eq "SafeExamBrowser"} | Select-Object -First 1
$sebWindow.MainWindowHandle
$sebWindow.MainWindowHandle = $sebWindow.MainWindowHandle.ToInt32()
$sebWindow.MainWindowHandle.ToInt32()

# Set the Safe Exam Browser window to be a "non-locking" window
Add-Type -Name Window -Namespace Console -MemberDefinition @"
[DllImport("user32.dll")]
public static extern int SetWindowLong(IntPtr hWnd, int nIndex, int dwNewLong);
"@

SetWindowLong($sebWindow.MainWindowHandle, (-20), 0x20)

# Start the Safe Exam Browser process
$sebWindow.Start()
