import QtQuick
import QtQuick.Window

Window {
    property int w: 600
    property int h: 255

    id: window
    visible: true
    width: w
    height: h
    color: "#00000000"
    flags: Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint


    function main() {
        startAnim.start()
    }

    onActiveChanged: {
        if (!active) {
            endAnim.start()
        }
    }


    Rectangle {
        id: body
        color: "#1e1e1e"
        radius: 10
        border.width: 0
        anchors.fill: parent

        CustomButton {
            id: shutdown
            bg: "#d03535"
            image: "shutdown.png"
            opacity: 0
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: reboot.left
            anchors.rightMargin: window.width/10

            function onClick() {
                shutdownbackend.shutdown()
            }
        }

        CustomButton {
            id: reboot
            color: "#71c73e"
            bg: "#3dde3c"
            image: "reboot.png"
            opacity: 0
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter

            function onClick() {
                shutdownbackend.reboot()
            }
        }

        CustomButton {
            id: sleep
            bg: "#e9b22e"
            image: "sleep.png"
            opacity: 0
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: reboot.right
            anchors.leftMargin: window.width/10

            function onClick() {
                shutdownbackend.sleep()
            }
        }
    }

    ParallelAnimation {
        id: startAnim

        PropertyAnimation {
            target: window
            property: "width"
            from: 0
            to: w
            easing.type: Easing.OutCirc
            duration: 1000
        }
        PropertyAnimation {
            target: body
            property: "opacity"
            from: 0
            to: 1
            easing.type: Easing.OutCubic
            duration: 700
        }
        SequentialAnimation{

            PauseAnimation {
                duration: 300
            }
            ParallelAnimation {
                PropertyAnimation {
                    target: shutdown
                    property: "opacity"
                    from: 0
                    to: 1
                    easing.type: Easing.Linear
                    duration: 1000
                }
                PropertyAnimation {
                    target: reboot
                    property: "opacity"
                    from: 0
                    to: 1
                    easing.type: Easing.Linear
                    duration: 1000
                }
                PropertyAnimation {
                    target: sleep
                    property: "opacity"
                    from: 0
                    to: 1
                    easing.type: Easing.Linear
                    duration: 1000
                }
            }
        }
    }

    ParallelAnimation {
        id: endAnim

        onFinished: {
            window.hide()
        }

        PropertyAnimation {
            target: window
            property: "width"
            from: w
            to: 0
            easing.type: Easing.InSine
            duration: 1500
        }
        PropertyAnimation {
            target: body
            property: "opacity"
            from: 1
            to: 0
            easing.type: Easing.InSine
            duration: 1300
        }
    }
}



/*##^##
Designer {
    D{i:0;formeditorZoom:1.66}
}
##^##*/
