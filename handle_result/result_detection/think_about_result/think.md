将分数低于0.1的框过滤之后，LAMR从0.45降低到了0.288,剧烈的改变，

说明了什么？
我观察一下。

被过滤掉的，一般都是检测分数很低的框0.000(怎么会有这么多，分数为0.000的框，这是怎么回事？) 的那种，这些框，只能是带来误检，没有别的作用


是否再过滤掉一些，会更有效？

将分数调到0.5后，再过滤掉一些后，分数到达了0.298,这说明，TP也被过滤掉了，应该了结果，没有变好，反而变坏。

接下来的思路：
    本上记录了
    ２０１８年０６月１１日１７：３７：４０
    
通过观察，全身检测不到的，通过上半身，也检测不到。。那么这样就不能通过使用上半身检测来提高recall.

原本通过检测上半身就可以达到0.25,检测全身达到0.28

可以尝试一下，基于现在最好的模型，然后使用部件检测,可以达到什么样的值？
