phone=document.getElementById('phone')
pass=document.getElementById('pass')

login={
    '9726989305':'pass123','8866778000':'pass123'
}
if (phone in login){
    if(pass==phone[pass]){
        console.log("login successfull")
    }
    else{
        console.log("pass incorrect")
    }
}
else {
    console.log("phone incorrect")
}