
const roomName = JSON.parse(document.getElementById('room-name').textContent);
const userName = JSON.parse(document.getElementById('username').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chats/'
    + roomName
    + '/'
);


let MsgLog=document.querySelector('#chat-log');
MsgLog.scrollTop=MsgLog.scrollHeight;
// alert("log:", MsgLog.innerHTML);

chatSocket.addEventListener('open', (e) => {
    console.log('Opened Connection!!!');
});

chatSocket.onmessage = function (e) {
    var data = JSON.parse(e.data);
    let response_type = data.type
    if (response_type == 'msg') {

        let sent_by;
        let display_msg;
        let tmp;
        if (data.sender == userName) {
            sent_by = 'self';
            tmp = "me"
        }
        else {
            sent_by = 'other';
            tmp = data.sender
        }
        console.log(data)
        display_msg = '<div class="' + sent_by + '">' + tmp + ': ' + data.message + '</div>';
        console.log(display_msg);
        MsgLog.innerHTML += display_msg;
        MsgLog.scrollTop=MsgLog.scrollHeight;
    }

};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly', e);
};

document.querySelector('#chat-message-input').focus();

document.querySelector('#chat-message-input').addEventListener('keyup', function (e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
});

document.querySelector('#chat-message-submit').addEventListener('click', function (e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'type': 'msg',
        'sender': userName,
        'message': message
    }));
    messageInputDom.value = '';
});
