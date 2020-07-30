# method1
for param in model.parameters():
    param.requires_grad = False
optimizer = optim.SGD(model.fc.parameters(), lr=0.05, momentum=0.9)

# method2
for param in model.parameters():
    param = param.detach()

# sanity check
for name, params in net.named_parameters():
    print(name,params.requires_grad, \params.grad)
