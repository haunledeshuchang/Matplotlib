import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim([1,7])
ax.set_ylim([1,5])
ax.text(2,4,r'$ \alpha_i \beta_j \lambda \pi $',size=25)
ax.text(4,4,r'$  \sin(0)= \cos(\frac {\pi} {2}) $',size=25)
ax.text(2,2,r'$ \lim_(x \rightarrow y) \frac {1}{x^3} $',size=25)
ax.text(5,2,r'$ \sqrt[3]{x}=\sqrt{x} $',size=25)

