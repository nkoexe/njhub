import QtQuick
import QtQuick.Window

Window {
    id: window
    visible: true
    x: -1920
    y: 340
    width: 1920
    height: 450
    color: "#00000000"
    flags: Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowTransparentForInput


    // ~ Animation properties

    // Animation duration
    property int d0: 650  // opening
    property int d1: 800  // closing

    // Rectangele 1
    property int r1x0: -80   // initial x
    property int r1x1: -62   // final x
    property int r1y0: -318  // initial y
    property int r1y1: -158  // final y
    property int r1r0: 0     // initial rotation
    property int r1r1: -13   // final rotation

    // Rectangle 2
    property int r2x0: -80   // initial x
    property int r2x1: -78   // final x
    property int r2y0: -191  // initial y
    property int r2y1: 31    // final y
    property int r2r0: 0     // initial rotation
    property int r2r1: -16   // final rotation

    // Title
    property int t1x0: 0   // initial x
    property int t1x1: 35  // final x
    property int t1o0: 0   // initial opacity
    property int t1o1: 1   // final opacity
    // Text
    property int t2x0: 0   // initial x
    property int t2x1: 30  // final x
    property int t2o0: 0   // initial opacity
    property int t2o1: 1   // final opacity


    function notify(t, m, d) {
        title.text = t
        content.text = m
        timer.interval = d

        window.show()
        startAnim.start()
        timer.start()
    }

    function end() {
        endAnim.start()
        endAnim.finished.connect(function() {
            window.hide()
        })
    }

    Timer {
        id: timer
        onTriggered: end()
    }

    Rectangle {
        id: body
        color: "#001e1e1e"
        anchors.fill: parent
        clip: true

        Rectangle {
            id: rectangle2
            x: r2x0
            y: r2y0
            width: 1600
            height: 186
            color: "#343434"
            rotation: r2r0
        }

        Rectangle {
            id: rectangle1
            x: r1x0
            y: r1y0
            width: 1390
            height: 314
            color: "#1d1d1d"
            rotation: r1r0
        }

        Text {
            id: title
            opacity: 0
            color: "#ffffff"
            text: qsTr("Notification Title")
            font.pixelSize: 30
            font.family: "Product Sans"
            wrapMode: Text.WordWrap
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.topMargin: 40
            anchors.leftMargin: t1x0
        }

        Text {
            id: content
            width: 536
            opacity: 0
            color: "#ffffff"
            text: qsTr("This is the notification text!")
            font.pixelSize: 24
            font.family: "Product Sans"
            wrapMode: Text.WordWrap
            anchors.top: title.bottom
            anchors.left: parent.left
            anchors.topMargin: 10
            anchors.leftMargin: t2x0
        }


        ParallelAnimation {
            id: startAnim

            PropertyAnimation {
                target: rectangle1
                property: "x"
                to: r1x1
                easing.type: Easing.OutExpo
                duration: d0
            }
            PropertyAnimation {
                target: rectangle1
                property: "y"
                to: r1y1
                easing.type: Easing.OutExpo
                duration: d0
            }
            PropertyAnimation {
                target: rectangle1
                property: "rotation"
                to: r1r1
                easing.type: Easing.OutExpo
                duration: d0
            }

            PropertyAnimation {
                target: rectangle2
                property: "x"
                to: r2x1
                easing.type: Easing.OutExpo
                duration: d0
            }
            PropertyAnimation {
                target: rectangle2
                property: "y"
                to: r2y1
                easing.type: Easing.OutExpo
                duration: d0
            }
            PropertyAnimation {
                target: rectangle2
                property: "rotation"
                to: r2r1
                easing.type: Easing.OutExpo
                duration: d0
            }

            PropertyAnimation {
                target: title
                property: "anchors.leftMargin"
                to: t1x1
                easing.type: Easing.OutExpo
                duration: d0
            }
            PropertyAnimation {
                target: title
                property: "opacity"
                to: t1o1
                easing.type: Easing.OutExpo
                duration: d0
            }
            SequentialAnimation {
                PauseAnimation {duration: 100}
                PropertyAnimation {
                    target: content
                    property: "anchors.leftMargin"
                    to: t2x1
                    easing.type: Easing.OutExpo
                    duration: d0
                }
            }

            SequentialAnimation {
                PauseAnimation {duration: 100}
                PropertyAnimation {
                    target: content
                    property: "opacity"
                    to: t2o1
                    easing.type: Easing.OutExpo
                    duration: d0
                }
            }
        }


        ParallelAnimation {
            id: endAnim

            PropertyAnimation {
                target: rectangle1;
                property: "x"
                to: r1x1
                easing.type: Easing.OutExpo;
                duration: d1
            }
            PropertyAnimation {
                target: rectangle1;
                property: "y"
                to: r1y0
                easing.type: Easing.OutExpo;
                duration: d1
            }
            PropertyAnimation {
                target: rectangle1;
                property: "rotation"
                to: r1r0
                easing.type: Easing.OutExpo;
                duration: d1
            }

            PropertyAnimation {
                target: rectangle2;
                property: "x"
                to: r2x0
                easing.type: Easing.OutExpo;
                duration: d1
            }
            PropertyAnimation {
                target: rectangle2;
                property: "y"
                to: r2y0
                easing.type: Easing.OutExpo;
                duration: d1
            }
            PropertyAnimation {
                target: rectangle2;
                property: "rotation"
                to: r2r0
                easing.type: Easing.OutExpo;
                duration: d1
            }

            PropertyAnimation {
                target: title
                property: "anchors.leftMargin"
                to: t1x0
                easing.type: Easing.OutExpo
                duration: d1
            }
            PropertyAnimation {
                target: title
                property: "opacity"
                to: t1o0
                easing.type: Easing.OutExpo
                duration: d1
            }
            PropertyAnimation {
                target: content
                property: "anchors.leftMargin"
                to: t2x0
                easing.type: Easing.OutExpo
                duration: d1
            }
            PropertyAnimation {
                target: content
                property: "opacity"
                to: t2o0
                easing.type: Easing.OutExpo
                duration: d1
            }
        }

    }
}



/*##^##
Designer {
    D{i:0;formeditorZoom:0.66}
}
##^##*/
